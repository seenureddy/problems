package main


import (
    "fmt"
    "os"
	"strings"
	"sort"
	"io/ioutil"
)


func checkError(e error) {
	if e != nil {
		panic(e)
	}
}

func repetition(lines []string) map[string]int {
  
    wc := make(map[string]int)
	for i := 0; i < len(lines); i++ {

		word := strings.ReplaceAll(lines[i], " ", "")

		if word == "" {
			continue
		}
		
		word1 := strings.TrimSpace(word)
		_, matched := wc[word1]
        if matched {
            wc[word1] += 1
        } else {
            wc[word1] = 1
        }
	}
  
    return wc
}

func sortMapByValue(counts map[string]int) (map[string]int, []string){
	keys := make([]string, 0, len(counts))
    for key := range counts {
        keys = append(keys, key)
    }
    sort.Slice(keys, func(i, j int) bool { return counts[keys[i]] > counts[keys[j]] })
	return counts, keys
}


func main() {
	argsWithoutProg := os.Args[1:]
	// fmt.Println(argsWithoutProg)

	file_data, err := ioutil.ReadFile(argsWithoutProg[0])
	checkError(err)
	
	lines := strings.Split(string(file_data), " ")
	countsData := repetition(lines)

	
	sortedCountData, keys := sortMapByValue(countsData)

    for index, key := range keys {
		if sortedCountData[key] == 1 {
			continue
		}
		if index <= 10 {
			fmt.Printf("   %d %s\n", sortedCountData[key], key)
		}
    }
}
