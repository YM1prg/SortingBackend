from flask import Flask, request, jsonify
from flask_cors import CORS
from Algorithums_folder.Bubble import bubble_sort_with_steps
from Algorithums_folder.insertion import insertion_sort_with_steps
from Algorithums_folder.Selection import selection_sort_with_steps
from Algorithums_folder.Quick import quick_sort_with_steps

app = Flask(__name__)
CORS(app)

# تعريف معلومات التعقيد الزمني للخوارزميات
ALGORITHM_INFO = {
    'bubble': {
        'name': 'Bubble Sort',
        'timeComplexity': 'O(n²)',
        'spaceComplexity': 'O(1)',
        'description': "Compares adjacent elements and swaps them if they are in the wrong order. Repeats until the list is sorted. Also simple but slow for large datasets."
    },
    'selection': {
        'name': 'Selection Sort',
        'timeComplexity': 'O(n²)',
        'spaceComplexity': 'O(1)',
        'description':"Repeatedly finds the minimum element from the unsorted part and moves it to the beginning. Simple but inefficient for large lists."
    },
    'insertion': {
        'name': 'Insertion Sort',
        'timeComplexity': 'O(n²)',
        'spaceComplexity': 'O(1)',
        'description': "Builds the final sorted array one item at a time by inserting each element into its correct position. Efficient for small or nearly sorted datasets."
    },
    'quick': {
        'name': 'Quick Sort',
        'timeComplexity': 'O(n log n)',
        'spaceComplexity': 'O(log n)',
        'description': "Uses a divide-and-conquer approach by selecting a 'pivot' element and partitioning the array around the pivot, sorting the sub-arrays recursively. Fast on average and works well with large datasets."
    }
}

@app.route('/sort', methods=['POST'])
def sort():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        array = data.get('array', [])
        algorithm = data.get('algorithm', 'bubble')

        if not array:
            return jsonify({"error": "No array provided"}), 400
            
        if not isinstance(array, list):
            return jsonify({"error": "Array must be a list"}), 400
            
        try:
            array = [float(x) for x in array]
        except (ValueError, TypeError):
            return jsonify({"error": "Array must contain only numbers"}), 400

        if algorithm == 'bubble':
            sorted_array, steps, execution_time = bubble_sort_with_steps(array)
        elif algorithm == 'selection':
            sorted_array, steps, execution_time = selection_sort_with_steps(array)
        elif algorithm == 'insertion':
            sorted_array, steps, execution_time = insertion_sort_with_steps(array)
        elif algorithm == 'quick':
            sorted_array, steps, execution_time = quick_sort_with_steps(array)
        else:
            return jsonify({"error": f"Invalid algorithm: {algorithm}. Supported algorithms: bubble, selection, insertion, quick"}), 400

        return jsonify({
            "sortedArray": sorted_array,
            "steps": steps,
            "algorithm": algorithm,
            "algorithmInfo": ALGORITHM_INFO[algorithm],
            "executionTime": execution_time,
            "originalArray": array
        })

    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

@app.route('/algorithms', methods=['GET'])
def get_algorithms():
    return jsonify(ALGORITHM_INFO)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
