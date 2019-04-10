from leapp.libraries.common import reporting

def generate_report():
    title = ''
    severity = '' # low/medium/high
    summary = ''

    # Many different reports available, see:
    # https://github.com/oamg/leapp-repository/blob/master/repos/system_upgrade/el7toel8/libraries/reporting.py
    reporting.report_generic(title=title, severity=severity, summary=summary)
