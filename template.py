class Template:
    def __init__(self, before_term="", before_defs=" -- ", before_pos="(", before_list=") ", use_numbers=True, before_def=". ", after_def=" ", after_list="", after=""):
        self.before_term = before_term
        self.before_defs = before_defs
        self.before_pos = before_pos
        self.before_list = before_list
        self.use_numbers = use_numbers
        self.before_def = before_def
        self.after_def = after_def
        self.after_list = after_list
        self.after = after
        
multiline = Template(before_defs=":", before_pos="\n  ", before_list="", use_numbers = False, before_def="\n    ", after_list = "\n")