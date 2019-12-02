from leapp.snactor.fixture import current_actor_context
from leapp.models import InstalledRedHatSignedRPM, RPM
from leapp.reporting import Report


def _generate_rpm_with_name(name):
    """
    Generate new RPM model item with given name.

    Parameters:
        name (str): rpm name

    Returns:
        rpm  (RPM): new RPM object with name parameter set

    """
    return RPM(name=name,
               version='0.1',
               release='1.sm01',
               epoch='1',
               pgpsig='RSA/SHA256, Mon 01 Jan 1970 00:00:00 AM -03, Key ID 199e2f91fd431d51',
               packager='Red Hat, Inc. <http://bugzilla.redhat.com/bugzilla>',
               arch='noarch')


def _test_actor_execution(current_actor_context, has_server=False, has_contrib=False):
    """
    Parametrized helper function for test_actor_* functions.

    First generate list of RPM models based on set arguments. Then, run
    the actor feeded with our RPM list. Finally, assert Reports
    according to set arguments.

    Parameters:
        has_server  (bool): postgresql-server installed
        has_contrib (bool): postgresql-contrib installed

    """

    # Couple of random packages
    rpms = [_generate_rpm_with_name('sed'),
            _generate_rpm_with_name('htop')]

    if has_server:
        # Add postgresql-server
        rpms += [_generate_rpm_with_name('postgresql-server')]
        if has_contrib:
            # Add postgresql-contrib
            rpms += [_generate_rpm_with_name('postgresql-contrib')]

    # Executed actor feeded with out fake RPMs
    current_actor_context.feed(InstalledRedHatSignedRPM(items=rpms))
    current_actor_context.run()

    if has_server and has_contrib:
        # Assert for postgresql-server and postgresql-contrib packages installed
        assert current_actor_context.consume(Report)
    elif has_server:
        # Assert only for postgresql-server package installed
        assert current_actor_context.consume(Report)
    else:
        # Assert for no postgresql packages installed
        assert not current_actor_context.consume(Report)


def test_actor_without_postgresql_server(current_actor_context):
    """
    Test actor execution without both server and contrib packages installed.

    Without:
        postgresql-server
        postgresql-contrib

    """
    _test_actor_execution(current_actor_context, False)


def test_actor_with_postgresql_server(current_actor_context):
    """
    Test actor execution with only server package installed.

    With:
        postgresql-server

    Without:
        postgresql-contrib

    """
    _test_actor_execution(current_actor_context, True, False)


def test_actor_with_postgresql_contrib(current_actor_context):
    """
    Test actor execution with both server and contrib packages installed.

    With:
        postgresql-server
        postgresql-contrib

    """
    _test_actor_execution(current_actor_context, True, True)
