
# ===============================================
# SOAL 5: Graph Models & Simple Cycle Detection
# ===============================================

class Node:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


class Edge:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

    def __repr__(self):
        return f"({self.node1}-{self.node2})"


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, node1, node2):
        """Tambahkan edge tak berarah"""
        if node1 not in self.adj_list:
            self.adj_list[node1] = []
        if node2 not in self.adj_list:
            self.adj_list[node2] = []

        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)

    def __repr__(self):
        return "\n".join(f"{n}: {nbrs}" for n, nbrs in self.adj_list.items())

    def find_simple_cycle(self):
        """Cari salah satu siklus sederhana (DFS rekursif)"""
        visited = set()
        path = []

        def dfs(current, parent):
            visited.add(current)
            path.append(current)

            for neighbor in self.adj_list.get(current, []):
                if neighbor == parent:
                    continue  # abaikan edge balik
                if neighbor in path:
                    # ditemukan siklus sederhana
                    cycle_start = path.index(neighbor)
                    return path[cycle_start:] + [neighbor]
                if neighbor not in visited:
                    result = dfs(neighbor, current)
                    if result:
                        return result

            path.pop()
            return None

        # Mulai DFS dari setiap node untuk memastikan graph tak terhubung juga bisa
        for node in self.adj_list:
            if node not in visited:
                cycle = dfs(node, None)
                if cycle:
                    return cycle
        return None


# --- Contoh Pengujian Soal ---
edges = {(1, 2), (2, 3), (3, 4), (1, 4), (1, 3)}

graph = Graph()
for n1, n2 in edges:
    graph.add_edge(n1, n2)

print("=== Struktur Graph ===")
print(graph)

cycle = graph.find_simple_cycle()

print("\n=== Siklus Sederhana yang Ditemukan ===")
if cycle:
    print(" => ".join(map(str, cycle)))
else:
    print("Tidak ada siklus sederhana.")
