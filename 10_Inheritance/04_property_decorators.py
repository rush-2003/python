# In Python, a **property decorator** (`@property`) is used to create getter, setter, and deleter methods 
# in a class in a Pythonic way. It allows you to access class methods as if they were attributes, 
# which improves code readability and encapsulation.

# ### How `@property` Works

# 1. **Getter**: Access the value of an attribute via a method.
# 2. **Setter**: Set the value of an attribute via a method.
# 3. **Deleter**: Delete an attribute using a method.

# ### Benefits
# - Encapsulation: You can control how attributes are accessed and modified.
# - Simplified Syntax: You can access methods as if they were attributes.
# - Backward Compatibility: Enables transition from public attributes to computed attributes without changing the interface.

# ### Example


class Circle:
    def __init__(self, radius):
        self._radius = radius  # Using a protected attribute for internal storage

    # Getter method
    @property
    def radius(self):
        return self._radius

    # Setter method
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    # Deleter method
    @radius.deleter
    def radius(self):
        print("Deleting radius...")
        self._radius = None

# Usage
c = Circle(5)

print(c.radius)  # Accessing via the getter
c.radius = 10    # Modifying via the setter
print(c.radius)

del c.radius      # Deleting via the deleter



### Key Points:
# - Use `@property` for the getter.
# - Use `@property_name.setter` for the setter.
# - Use `@property_name.deleter` for the deleter.
# - The original attribute (e.g., `_radius`) should usually be private or protected (indicated by a leading underscore).