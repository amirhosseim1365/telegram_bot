from datetime import datetime



def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ('hello','hi','sup'):
        return 'Hey! How is it going?'
    
    return 'سلام چطوری؟'