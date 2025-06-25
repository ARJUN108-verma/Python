# Global scope
x = "global"

def outer_function():
    # Enclosing scope
    x = "enclosing"

    def inner_function():
        # Local scope
        x = "local"
        print("Inner Function (Local Scope):", x)

    inner_function()
    print("Outer Function (Enclosing Scope):", x)

outer_function()
print("Global Scope:", x)

