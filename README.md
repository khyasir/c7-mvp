# Workflow Diagnoser

The live-build artifact from Cohort 7, Lecture 05. Describe one repeated task,
get back a structured workflow diagnosis on screen.

Today there is NO LLM. `diagnose()` is a mock that returns a fixed sample answer
so we can focus on one thing: building an interface that takes an input and shows
an output. In a later session we swap the inside of `diagnose()` for a real model
call. Nothing else changes.

## Files

- `diagnoser.py` - the system. Plain Python. A mock for now. Run it alone to test in the terminal.
- `app_gradio.py` - the Gradio interface over the system.
- `app_streamlit.py` - the Streamlit interface over the same system.
- `requirements.txt` - what to install.

## Setup (once)

```
pip install -r requirements.txt
```

No API key needed today. The system is mocked.

## Run

Test the system with no interface:

```
python diagnoser.py
```

Run the Gradio interface:

```
python app_gradio.py
```

Run the Streamlit interface:

```
streamlit run app_streamlit.py
```

Each app prints a local URL. Open it in your browser.

## What comes later

The body of `diagnose()` is the only thing that becomes a real LLM call in a
future session. The interface, the input filter, and the output format all stay
exactly as they are. That is the point of keeping the system behind one function.
