from graph import graph

if __name__ == '__main__':
    test = graph()
    #test.readFromJson("{\"nodes\" : \"5\",\"edges\" : [ { \"node\": \"1\", \"edge\": \"2 5\" },{ \"node\": \"2\", \"edge\": \"4\" }, { \"node\": \"3\", \"edge\": \"4\" }, { \"node\": \"5\", \"edge\": \"3\" } ] }")
    test.readFromJson()