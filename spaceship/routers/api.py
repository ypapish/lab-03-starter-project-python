from fastapi import APIRouter

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}


@router.get('/matrix')
def matrix_multiply():
    matrix_a = np.random.rand(10, 10).tolist()
    matrix_b = np.random.rand(10, 10).tolist()
    return {
        "matrix_a": matrix_a,
        "matrix_b": matrix_b,
        "product": np.dot(matrix_a, matrix_b).tolist()
    }