class Object():
    def __init__(self, obj):
        process_retention_param(obj.get("retention"))
        self.retention = obj.get("retention")
        self.id = 0
        process_username(obj.get("username"))
        self.username = obj.get("user")
        
def process_retention_param(args, parser_object):
    if hasattr(args, "retention") and len(args.retention) >= 3:
        parser_object.error('The "--retention or -r" parameter must have max two integers. Three or more arguments specified: {}'.format(args.retention))

def process_username(args, parser_object):
    if not hasattr(args, "username"):
        parser_object.error('The username argument must be specified')