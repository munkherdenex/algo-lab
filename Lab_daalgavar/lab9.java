import java.util.Stack;

class Lab9 {
    static class MyQueue {
        private Stack<Integer> stackIn; 
        private Stack<Integer> stackOut; 

        public MyQueue() {
            stackIn = new Stack<>();
            stackOut = new Stack<>();
        }

        public void push(int x) {
            stackIn.push(x);
        }

        public int pop() {
            if (stackOut.isEmpty()) {
                while (!stackIn.isEmpty()) {
                    stackOut.push(stackIn.pop());
                }
            }
            return stackOut.pop();
        }

        public int peek() {
            if (stackOut.isEmpty()) {
                while (!stackIn.isEmpty()) {
                    stackOut.push(stackIn.pop());
                }
            }
            return stackOut.peek();
        }

        public boolean empty() {
            return stackIn.isEmpty() && stackOut.isEmpty();
        }
    }

    public static void main(String[] args) {
        MyQueue myQueue = new MyQueue();

        myQueue.push(1);  
        myQueue.push(2);  

        System.out.println("Peek: " + myQueue.peek()); 
        System.out.println("Pop: " + myQueue.pop());    
        System.out.println("Is empty: " + myQueue.empty()); 
    }
}
