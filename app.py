from flask import Flask, request, jsonify
from flask_cors import CORS
from Algorithums_folder.Bubble import bubble_sort_with_steps
from Algorithums_folder.insertion import insertion_sort_with_steps
from Algorithums_folder.Selection import selection_sort_with_steps
from Algorithums_folder.Quick import quick_sort_with_steps

app = Flask(__name__)
CORS(app)

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
            sorted_array, steps = bubble_sort_with_steps(array)
        elif algorithm == 'selection':
            sorted_array, steps = selection_sort_with_steps(array)
        elif algorithm == 'insertion':
            sorted_array, steps = insertion_sort_with_steps(array)
        elif algorithm == 'quick':
            sorted_array, steps = quick_sort_with_steps(array)
        else:
            return jsonify({"error": f"Invalid algorithm: {algorithm}. Supported algorithms: bubble, selection, insertion, quick"}), 400

        return jsonify({
            "sortedArray": sorted_array,
            "steps": steps,
            "algorithm": algorithm,
            "originalArray": array
        })

    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')