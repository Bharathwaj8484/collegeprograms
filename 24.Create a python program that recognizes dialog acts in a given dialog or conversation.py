def recognize_dialog_acts(utterance):
    if "?" in utterance:
        return "Question"
    elif "!" in utterance:
        return "Exclamation"
    else:
        return "Statement"
utterance = "How are you doing?"
act = recognize_dialog_acts(utterance)
print(f"Dialog Act: {act}")
