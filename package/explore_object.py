def check_dir(obj):
    print ("="*90, f"\nPRINTING attr's FROM {obj.__class__}\n", "="*90, "\n")
    for attr_name in dir(obj):
        attr_value = getattr(obj, attr_name)
        msg = "> {}:\n{} | Callable:{}".format(attr_name, attr_value, callable(attr_value))
        print(msg)
    print("="*90, "\n")