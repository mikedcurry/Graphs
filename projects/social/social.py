import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    #Basically the same as edges, only they're bi-directional
    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            # Here's that bi-directional part
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    # Basically a special case of a vertex with ID info and possibility for store friendships???
    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()
        # self.vertices[vertex_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        ## Where my code begins... ##

        # Add users
        for i in range(0, num_users):
            self.add_user(f'User {i}')

        possible_friendships = [] # Unless you're me, then this list is always empty...
        
        # Create friendships
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                 possible_friendships.append((user_id, friend_id))

        # as per spec, suffle possible friendships. In place. 
        random.shuffle(possible_friendships)

        # make friendships...
        for j in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[j]
            self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        ## My code from here on ##
        q = Queue()
        q.enqueue([user_id])

        while q.size():
            path = q.dequeue()

            v = path[-1]
            
            # When we find unvisited nodes...
            if v not in visited:
                # add path to visited
                visited[v] = path

                # add all the neighboring vertices to the queue
                for neighbor in self.friendships[v]:
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
