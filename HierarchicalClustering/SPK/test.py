data = {}
data.setdefault("id", 0)   # duplicate
data.setdefault("data", [1,2,3,4])
data.setdefault("class", 1)

for keys, values in data.items():
    print (keys),(values)

id = 0
clusters_key = str([id])
clusters = {}
clusters.setdefault(clusters_key, {})
clusters[clusters_key].setdefault("centroid", [4])
clusters[clusters_key].setdefault("elements", [id])

for keys, values in clusters.items():
    print (values)


