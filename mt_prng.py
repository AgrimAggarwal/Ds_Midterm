(w, n, m, r) = (32, 624, 397, 31)
a = 0x9908B0DF
(u, d) = (11, 0xFFFFFFFF)
(s, b) = (7, 0x9D2C5680)
(t, c) = (15, 0xEFC60000)
l = 18
f = 1812433253

# Create a length n array to store the state of the generator
MT = []
for i in range(n):
    MT.append(0)

index = n + 1
lower_mask = 0xFFFFFFFF
upper_mask = 0x00000000

# Initialize the generator from a seed


def mt_seed(seed):
    MT[0] = seed
    for i in range(1, n):
        temp = f * (MT[i - 1] ^ (MT[i - 1] >> (w - 2))) + i
        MT[i] = temp & lower_mask


# Extract a tempered value based on MT[index]
# calling twist() every n numbers
def extract_number():
    global index
    if index >= n:
        twist()
        index = 0

    y = MT[index]
    y = y ^ ((y >> u) & d)
    y = y ^ ((y << t) & c)
    y = y ^ ((y << s) & b)
    y = y ^ (y >> l)

    index += 1
    return y & lower_mask


# Generate the next n values from the series x_i
def twist():
    for i in range(0, n):
        x = (MT[i] & upper_mask) + (MT[(i+1) % n] & lower_mask)
        xA = x >> 1
        if (x % 2) != 0:
            xA = xA ^ a
        MT[i] = MT[(i + m) % n] ^ xA


def random():
    return extract_number() / (2 ** w)


def randint(a, b):
    org = random()
    return int((org*(b-a)) + a)


def mt_choice(seq, size=1, replace=True):
    temp = list(seq)
    if size == 1:
        return temp[randint(0, len(seq))]
    else:
        if replace:
            return [temp[randint(0, len(seq))] for i in range(size)]
        else:
            temp2 = []
            for _ in range(size):
                if len(temp) != 0:
                    a = randint(0, len(temp))
                    temp2 += [temp[a]]
                    temp.remove(temp[a])
            return temp2
