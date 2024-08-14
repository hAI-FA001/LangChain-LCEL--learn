from langchain_core.runnables import RunnablePassthrough, RunnableLambda, RunnableParallel


if __name__ == "__main__":
    data = "test"


    # passes the input through without any changes
    # useful when used with other Runnables
    chain = RunnablePassthrough() | RunnablePassthrough() | RunnablePassthrough()
    
    print(f"Passthrough: {chain.invoke(data)}")


    # can use any custom function
    def print_and_pass(x):
        print(x)
        return x
    to_upper = lambda x: x.upper()
    to_lower = lambda x: x.lower()

    chain = RunnableLambda(to_upper) | RunnableLambda(print_and_pass) \
    | RunnableLambda(to_lower) | RunnableLambda(print_and_pass) \
    | RunnableLambda(to_upper) | RunnableLambda(print_and_pass)
    
    print(f"Lambda: {chain.invoke(data)}")


    # used to perform 2 tasks on the same input
    # e.g. branching (test -> {upper: TEST, lower: test})
    chain = RunnableParallel({"upper": RunnableLambda(to_upper), "lower": RunnableLambda(to_lower)})
    print(f"Parallel: {chain.invoke(data)}")
    
    chain = RunnableParallel({"original": RunnablePassthrough(), "data": RunnableLambda(lambda x: x['data'])})
    print(f"Parallel on dict input: {chain.invoke({"a": "abc", "b": "bcd", "data": data})}")

    
    # nested chains
    chain = RunnableParallel({
        "a": RunnablePassthrough()
            | RunnableLambda(lambda x: x.get('data', 'no data'))
            | RunnableLambda(lambda x: x.upper()),
        "b": lambda x: x["other"]
    })
    
    print(f"\nNested: {chain.invoke({'other': 123, 'data': data})}")
    print(f"Nested (no data): {chain.invoke({'other': 123})}")

    
    # assign() adds key in chain
    chain = RunnableParallel({"a": RunnablePassthrough()})
    chain = chain.assign(new_key=RunnableLambda(lambda x: "some value"))
    
    print(f"\n.assign(): {chain.invoke(data)}")


    # Coercion
    chain = RunnablePassthrough() \
    | {"new_key": RunnablePassthrough()} \
    | (lambda x: {"new_key": "function has been coerced - " + x.get('new_key', 'no key')})
    
    print(f"Coercion: {chain.invoke("dict has been coerced into Runnable")}")
    