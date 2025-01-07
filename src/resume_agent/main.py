#!/usr/bin/env python
import sys
import warnings

from resume_agent.crew import ResumeAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
            """
            Run the crew.
            """
            
            inputs = { 'job_posting_url': 'https://jobs.lever.co/AIFund/6c82e23e-d954-4dd8-a734-c0c2c5ee00f1?lever-origin=applied&lever-source%5B%5D=AI+Fund'}
            try:
                ResumeAgent().crew().kickoff(inputs=inputs)
            except Exception as e:
                raise Exception("An error occurred while running the crew: {e}")