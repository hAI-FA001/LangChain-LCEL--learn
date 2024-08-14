# Learning LangChain Expression Language via Practice

<a href="https://www.youtube.com/watch?v=LzxSY7197ns">Tutorial followed</a>
<br>

Key Ideas:
<table>
  <tr>
    <td>a | b syntax</td>
    <td>This is achieved by overriding __or__ method</td>
  </tr>
  <tr>
    <td>RunnablePassthrough</td>
    <td>Pass the input as it is</td>
  </tr>
  <tr>
    <td>RunnableLambda</td>
    <td>For any custom function/logic</td>
  </tr>
  <tr>
    <td>RunnableParallel</td>
    <td>For creating multiple outputs from the same input</td>
  </tr>
  <tr>
    <td>Coercion (dictionary and functions are coerced into Runnable)</td>
    <td>{"example": "dict"} | RunnableLambda(lambda x: "example runnable") or lambda x: "example fn" | RunnableLambda(lambda x: "example runnable")</td>
  </tr>
  <tr>
    <td>my_chain.assign(key=some_runnable)</td>
    <td>for adding more keys to the output of the chain so far</td>
  </tr>
</table>
