def cipher(text, shift, encrypt=True):
    """
    This fuction conducts Caesar cipher 
    Casser cipher is one of the simplest and mose widely known encryption techniques. 
    Each letter is replaced by a letter some fixed number of positions down (encryptiont) or up (decription) the alphabet.
    
    Parameters
    ----------
    text : sting
    shift : int
    encrypt : boolean value (default : True)
          
    Returns
    -------
    string 
       New text encrypted/decrypted
       
    Examples
    --------
    >>> text = "ababa."
    >>> cipher(text = text, shift = 1, encrypt=True)
    'bcbcb.'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text