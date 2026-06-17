import os
import gradio as gr
import requests

BACKEND_URL = os.environ.get("BACKEND_URL", "https://c7-mvp-95fi.onrender.com/diagnose")


def diagnose(message, conversation_id):
    """Send one turn. `conversation_id` is gradio State: None on the first turn,
    then the id the backend gave us — so every later turn appends to the SAME
    conversation row instead of creating a new one."""
    try:
        payload = {"workflow_description": message}
        if conversation_id is not None:
            payload["conversation_id"] = conversation_id

        response = requests.post(BACKEND_URL, json=payload, timeout=60)
        response.raise_for_status()

        # Remember the conversation id the backend returns, for the next turn.
        new_id = response.headers.get("X-Conversation-Id", conversation_id)
        if new_id is not None:
            new_id = int(new_id)

        return response.text, new_id
    except requests.RequestException as e:
        return f"Could not reach the backend.\n\n{e}", conversation_id


with gr.Blocks(title="Workflow Diagnoser") as demo:
    gr.Markdown("# Workflow Diagnoser\nDescribe one repeated task you do at work.")

    # Holds the conversation id across turns. Cleared (-> None) when chat is cleared.
    convo_state = gr.State(None)
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox(placeholder="Describe one repeated task you do at work.", show_label=False)

    def respond(message, chat_history, conversation_id):
        reply, new_id = diagnose(message, conversation_id)
        chat_history = chat_history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": reply},
        ]
        return "", chat_history, new_id

    msg.submit(respond, [msg, chatbot, convo_state], [msg, chatbot, convo_state])

    # Clearing the chat must also drop the conversation id -> next message starts fresh.
    chatbot.clear(lambda: None, None, convo_state)


if __name__ == "__main__":
    demo.launch()
