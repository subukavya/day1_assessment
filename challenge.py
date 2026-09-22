"""A question none of the three systems was specifically designed for."""

from day1_lab.workflow import workflow
from day1_lab.agent import agent


QUESTION = (
    "I can pay Rs. 30,000. "
    "Which two courses can I take together within this budget?"
)


print("Q:", QUESTION)

print("\nWorkflow :", workflow(QUESTION))

print("\nAgent    :", agent(QUESTION))