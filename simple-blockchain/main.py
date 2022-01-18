import blockchain

bchain = blockchain.Blockchain()
t1 = bchain.new_transaction('Lucas', 'José', 100)
t2 = bchain.new_transaction('José', 'Lucas', 50)
t3 = bchain.new_transaction('Lucas', 'José', 25)
bchain.new_block(proof=23334)

t4 = bchain.new_transaction('José', 'Lucas', 35)
t5 = bchain.new_transaction('Lucas', 'José', 40)
t6 = bchain.new_transaction('José', 'Lucas', 15)
bchain.new_block(proof=22321)

print(bchain.chain)
