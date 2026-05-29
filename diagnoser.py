"""
The Workflow Diagnoser. The system, in plain Python.

No web framework lives in this file. No LLM yet either. Right now diagnose()
is a MOCK: it returns a believable, hard-coded answer so we can build and test
the interface today. In a later session we replace the inside of this one
function with a real model call. Nothing else in the project will need to change.

That is the whole idea: the interface talks to diagnose(). It does not care
whether diagnose() is faked or real.
"""


def diagnose(description):
    """Take a task description, return a diagnosis.

    MOCK for now. It does not read the description yet, it just returns a fixed
    example so the interface has something real to display. Later, the body of
    this function becomes a real LLM call. The inputs and outputs stay the same.
    """
    # Hard-coded sample answer. Pretend the model wrote this.
    fake_answer = {
        "trigger": "Monday morning, before the team review",
        "steps": [
            "Open the three dashboards",
            "Copy the weekly numbers into a spreadsheet",
            "Write a short summary",
            "Paste it into a slide and send it",
        ],
        "bottleneck": "Copying numbers by hand from three places",
        "output": "A weekly summary slide",
        "ai_can_help": ["Pulling the numbers", "Drafting the summary"],
        "keep_human": ["Final check before sending to the manager"],
        "verdict": "Worth automating. The copy and summary steps are repetitive and slow.",
    }
    return {"ok": True, "diagnosis": fake_answer}


def format_diagnosis(result):
    """Turn the result into readable text. Both interfaces use this one function."""
    if not result["ok"]:
        return "Could not diagnose this yet.\n\n" + result["error"]

    d = result["diagnosis"]

    def as_list(value):
        return "\n".join("  - " + str(item) for item in value)

    lines = [
        "WORKFLOW DIAGNOSIS",
        "",
        "Trigger: " + d["trigger"],
        "",
        "Steps:",
        as_list(d["steps"]),
        "",
        "Bottleneck: " + d["bottleneck"],
        "",
        "Output: " + d["output"],
        "",
        "Where AI can help:",
        as_list(d["ai_can_help"]),
        "",
        "Keep a human in the loop for:",
        as_list(d["keep_human"]),
        "",
        "Verdict: " + d["verdict"],
    ]
    return "\n".join(lines)


# Run this file directly to test the system in the terminal, with no interface.
#   python diagnoser.py
if __name__ == "__main__":
    sample = "Every Monday I copy numbers from three dashboards into a slide for my manager."
    print(format_diagnosis(diagnose(sample)))
