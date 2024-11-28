import hashlib
import math


def calculate_loot(seed, duration, action, rewards):
    # Calculate the number of completed actions
    actions_completed = math.floor(duration / action.duration)

    # Initialize loot dictionary
    loot = {}

    # Generate hashes for all actions
    def generate_reward_hash(seed, index):
        """Generate a hash value as a floating-point number between 0 and 1."""
        compact_hash = hashlib.sha256(f"{seed}{index}".encode()).digest()[:4]
        return int.from_bytes(compact_hash, "big") / 0xffffffff

    # Loop through rewards
    for reward in rewards:
        item_id = str(reward.item.id)

        # Ensure the item is in the loot dictionary
        if item_id not in loot:
            loot[item_id] = {"id": item_id, "quantity": 0}

        # Check each action's hash to determine drops
        for i in range(actions_completed):
            reward_hash = generate_reward_hash(seed, i)
            if reward_hash <= reward.drop_rate:
                loot[item_id]["quantity"] += reward.quantity

    return loot