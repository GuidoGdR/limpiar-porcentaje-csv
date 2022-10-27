from tools import extract_info, clear_info, paste_info

def manager():
    
    
    info = extract_info()


    info = clear_info(info, '%')

    paste_info(info)



manager()