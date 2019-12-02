from leapp.actors import Actor
from leapp.models import Report, InstalledRedHatSignedRPM
from leapp.tags import IPUWorkflowTag, ChecksPhaseTag
from leapp.libraries.common.rpms import has_package
from leapp.libraries.actor.library import report_installed_packages


class PostgresqlCheck(Actor):
    """
    Actor checking for presence of PostgreSQL installation.

    Provides user with information related to upgrading systems
    with PostgreSQL installed.

    """
    name = 'postgresql_check'
    consumes = (InstalledRedHatSignedRPM,)
    produces = (Report,)
    tags = (IPUWorkflowTag, ChecksPhaseTag)

    def process(self):
        # Produce reports according to detection of installed PostgreSQL packages
        report_installed_packages(has_server=has_package(InstalledRedHatSignedRPM, 'postgresql-server'),
                                  has_contrib=has_package(InstalledRedHatSignedRPM, 'postgresql-contrib'))
