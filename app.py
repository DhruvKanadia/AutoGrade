import threading
import time
import random

def submit_answer_sheet(student_id):
    print(f"Student {student_id} submitted the answer sheet online.")
    time.sleep(random.uniform(0.5, 1.5))

def send_to_evaluator(student_id, evaluator_id):
    print(f"Answer sheet of Student {student_id} sent to Evaluator {evaluator_id}.")
    time.sleep(random.uniform(0.5, 1.0))

def evaluate_paper(student_id, evaluator_id):
    print(f"Evaluator {evaluator_id} is evaluating Student {student_id}'s paper...")
    time.sleep(random.uniform(1.0, 2.0))
    marks = random.randint(40, 100)
    print(f"Evaluator {evaluator_id} assigned {marks} marks to Student {student_id}.")
    return marks

def update_results(student_id, marks):
    print(f"Results updated: Student {student_id} scored {marks} marks.\n")
    time.sleep(random.uniform(0.5, 1.0))

def process_student(student_id, evaluator_id):
    submit_answer_sheet(student_id)
    send_to_evaluator(student_id, evaluator_id)
    marks = evaluate_paper(student_id, evaluator_id)
    update_results(student_id, marks)

if __name__ == "__main__":
    total_students = 5
    total_evaluators = 2
    threads = []
    
    print("\n=== ONLINE PAPER EVALUATION SYSTEM SIMULATION ===\n")
    
    for student_id in range(1, total_students + 1):
        evaluator_id = random.randint(1, total_evaluators)
        t = threading.Thread(target=process_student, args=(student_id, evaluator_id))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print("\n=== Evaluation Completed! ===\n")
