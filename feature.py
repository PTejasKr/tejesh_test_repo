def greet(name: str) -> None:
    """
    Prints a personalized greeting message.

    Args:
        name (str): The name to include in the greeting.
    """
    try:
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        print(f"Hello, {name}!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    greet("World")