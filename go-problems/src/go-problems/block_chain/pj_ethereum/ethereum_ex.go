package main

import (
	"context"
	"fmt"
	"log"

	"github.com/ethereum/go-ethereum/common"
	"github.com/ethereum/go-ethereum/ethclient"
)

func main() {

	conn, err := ethclient.Dial("https://mainnet.infura.io")
	if err != nil {
		log.Fatalf("Whoops something went wrong! %s", err)
	}

	ctx := context.Background()
	tx, pending, _ := conn.TransactionByHash(ctx, common.HexToHash("0xb97dbd02bd10541995dcbc485bff23f22a17c0f076e32e4f5cedefef4450bf43"))
	if !pending {
		fmt.Println(tx)
	}
}
