class Counter:
    total_instances = 0

    def __init__(self, value=0):
        # Save value in the object.
        # Add one to total_instances.
        pass

    @classmethod
    def reset_total_instances(cls):
        # Set total_instances to zero.
        pass

    def get(self):
        # Return the counter value.
        pass

    def increment(self, amount=1):
        # Add amount to the counter value.
        pass

    def increment_temporarily(self, amount=1):
        # Return the counter value plus amount without changing it.
        pass
