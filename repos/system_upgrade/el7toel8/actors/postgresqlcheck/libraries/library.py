from leapp import reporting


# Title for postgresql-server report
report_server_inst_title = 'PostgreSQL (postgresql-server) has been detected on your system'
# Summary for postgresql-server report
report_server_inst_summary = 'PostgreSQL server component will be upgraded. Since ' \
                             'RHEL-8 includes PostgreSQL server 10 by default, ' \
                             'which is incompatible with 9.2 included in RHEL-7, ' \
                             'it is necessary to proceed with additional steps ' \
                             'for complete upgrade of the PostgreSQL data. Back-up ' \
                             'your data before proceeding with the upgrade and read ' \
                             'more about upgrade steps in the knowledge base article.'

# Link text for postgresql-server report
report_server_inst_link_title = 'Learn more in this KB article.'
# Link URL for postgresql-server report
report_server_inst_link_url = 'https://access.redhat.com/articles/4055641'

# List of dropped extensions from postgresql-contrib package
report_contrib_inst_dropext = ['dummy_seclabel', 'test_parser', 'tsearch2']

# Title for postgresql-contrib report
report_contrib_inst_title = 'PostgreSQL (postgresql-contrib) has been detected on your system'
# Summary for postgresql-contrib report
report_contrib_inst_summary = 'Please note that some extensions have been dropped from the ' \
                              'postgresql-contrib package and might not be available after upgrade:\n' \
                              '{}'.format('\n'.join(report_contrib_inst_dropext))


def _report_server_installed():
    """
    Create report on postgresql-server package installation detection.

    Should remind user about present PostgreSQL server package
    installation, warn them about necessary additional steps, and
    redirect them to online documentation for the upgrade process.

    """
    reporting.create_report([
        reporting.Title(report_server_inst_title),
        reporting.Summary(report_server_inst_summary),
        reporting.Severity(reporting.Severity.HIGH),
        reporting.Tags([reporting.Tags.SERVICES]),
        reporting.ExternalLink(title=report_server_inst_link_title,
                               url=report_server_inst_link_url)
        ])


def _report_contrib_installed():
    """
    Create report on postgresql-contrib package installation detection.

    Should remind user about present PostgreSQL contrib package
    installation and provide them with a list of extensions no longer
    shipped with this package.

    """
    reporting.create_report([
        reporting.Title(report_contrib_inst_title),
        reporting.Summary(report_contrib_inst_summary),
        reporting.Severity(reporting.Severity.HIGH),
        reporting.Tags([reporting.Tags.SERVICES])
        ])


def report_installed_packages(has_server=False, has_contrib=False):
    """
    Create reports according to detected PostgreSQL packages.

    Parameters:
        has_server  (bool): Is postgresql-server installed
        has_contrib (bool): Is postgresql-contrib installed

    """
    if has_server:
        # postgresql-server
        _report_server_installed()
        if has_contrib:
            # postgresql-contrib
            _report_contrib_installed()
