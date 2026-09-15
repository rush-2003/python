# Tower of Hanoi
# We are given 3 towers Source, Helper, Destination
# The source tower has some plates - lower plate is larger and top plate is comparatively smaller
# We have have to transfer the plates from source to destination and we can make use of helper tower
# But there are 2 conditions
# 1. We can pick one plate at a time
# 2. At any time no larger plate can be placed on the top of smaller plate

def towerOfHanoi(n, source, auxiliary, destination):

    # Base Condition
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Hypothesis + Induction Step 1
    towerOfHanoi(n - 1, source, destination, auxiliary)

    # Induction Step 2
    print(f"Move disk {n} from {source} to {destination}")

    # Induction Step 3
    towerOfHanoi(n - 1, auxiliary, source, destination)
    

towerOfHanoi(3, "A", "B", "C")
    
# Watch this video again
# Worth solving and understanding this question