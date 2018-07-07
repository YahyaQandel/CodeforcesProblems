wires = int(input())
birds_per_wire = list(map(int, input().rstrip().split()))
shooting_trials = int(input())

for i in range(0,shooting_trials):
    trial = list(map(int, input().rstrip().split()))

    wire_index = trial[0]-1
    if wire_index >0:
        birds_per_wire[wire_index -1] = (trial[1]-1) + birds_per_wire[wire_index -1]  # the wire above the targetted Oskol
    if (wire_index+1) < len(birds_per_wire):
        birds_per_wire[wire_index +1] = (birds_per_wire[wire_index] - trial[1]) + birds_per_wire[wire_index +1]      # the wire under the targetted Oskol
    birds_per_wire[wire_index] = 0                                                                     # targetted wire


for j in birds_per_wire:
    print(j)
