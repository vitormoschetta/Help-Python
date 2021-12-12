def execute(notifications: []):
    text = ''
    for item in notifications:
        text += item + ' | '
    return text

