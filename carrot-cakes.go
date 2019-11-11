package main

import (
	"fmt"
)

func Max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func main() {
	var n, t, k, d int
	fmt.Scanf("%d %d %d %d\n", &n, &t, &k, &d)
	numberOfTrials := (n + k - 1) / k;
	ovenOneStart := 0
	ovenTwoStart := d;
	for i := 0; i < numberOfTrials; i++ {
		if ovenOneStart <= ovenTwoStart {
			ovenOneStart += t
		} else {
			ovenTwoStart += t
		}
	}

	if Max(ovenOneStart, ovenTwoStart) < (numberOfTrials * t) {
		fmt.Print("YES")
	} else {
		fmt.Print("NO")
	}

}
