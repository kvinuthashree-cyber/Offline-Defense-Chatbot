from model_loader import load_qa_chain
from updater import auto_update_csv

def main():
    auto_update_csv()
    qa_chain = load_qa_chain()

    while True:
        question = input("❓ Ask a defense-related question (or type 'exit'): ")
        if question.lower() == "exit":
            break
        answer = qa_chain.run(question)
        print("💬", answer)

if __name__ == "__main__":
    main()
