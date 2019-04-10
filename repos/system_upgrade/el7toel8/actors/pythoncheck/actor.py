from leapp.actors import Actor
from leapp.reporting import Report
from leapp.tags import ChecksPhaseTag, IPUWorkflowTag

# Import from this actors' library
from leapp.libraries.actor.library import generate_report


class PythonCheck(Actor):
    """
    No documentation has been provided for the python_check actor.
    """

    name = 'python_check'
    consumes = ()
    produces = (Report,)
    tags = (IPUWorkflowTag, ChecksPhaseTag) # Run in check phase of IPU Workflow

    # Actors main function
    def process(self):
        generate_report()
