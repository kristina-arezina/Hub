import numpy as np

from hub.api.tensor import Tensor


def test_dynamic_tensor():
    t = Tensor(
        "./data/test/test_dynamic_tensor",
        mode="w",
        shape=(5, 100, 100),
        max_shape=(5, 100, 100),
        dtype="int32",
    )
    t[0, 80:, 80:] = np.ones((20, 20), dtype="int32")
    assert t[0, -5, 90:].tolist() == [1] * 10


def test_dynamic_tensor_2():
    t = Tensor(
        "./data/test/test_dynamic_tensor_2",
        mode="w",
        shape=(5, None, None),
        max_shape=(5, 100, 100),
        dtype="int32",
    )
    t[0] = np.ones((10, 10), dtype="int32")
    assert t[0, 5].tolist() == [1] * 10
    assert t[0, 5, :].tolist() == [1] * 10
    t[0, 6] = 2 * np.ones((20,), dtype="int32")
    assert t[0, 5, :].tolist() == [1] * 10 + [0] * 10


def test_dynamic_tensor_3():
    t = Tensor(
        "./data/test/test_dynamic_tensor_3",
        mode="w",
        shape=(5, None, None, None),
        max_shape=(5, 100, 100, 100),
        dtype="int32",
    )
    t[0, 5] = np.ones((20, 30), dtype="int32")
    t[0, 6:8, 5:9] = 5 * np.ones((2, 4, 30), dtype="int32")
    assert t[0, 5, 7].tolist() == [1] * 30
    assert t[0, 7, 8].tolist() == [5] * 30


def test_dynamic_tensor_shapes():
    t = Tensor(
        "./data/test/test_dynamic_tensor_4",
        mode="w",
        shape=(5, None, None),
        max_shape=(5, 100, 100),
        dtype="int32",
    )
    t[0] = np.ones((5, 10), dtype="int32")
    t[0, 6] = 2 * np.ones((20,), dtype="int32")
    assert t[0, -1].tolist() == [2] * 20


def test_dynamic_tensor_4():
    t = Tensor(
        "./data/test/test_dynamic_tensor_4",
        mode="w",
        shape=(5, None, None, None),
        max_shape=(5, 100, 100, 10),
        dtype="int32",
    )
    t[0, 6:8] = np.ones((2, 20, 10), dtype="int32")
    assert (t[0, 6:8] == np.ones((2, 20, 10), dtype="int32")).all()


def test_chunk_iterator():
    t = Tensor(
        "./data/test/test_dynamic_tensor_4",
        mode="w",
        shape=(50, 100, 100, 100),
        max_shape=(50, 100, 100, 100),
        dtype="int32",
    )

    assert t.chunksize == (5, 100, 100, 100)
    assert list(t.chunk_iterator())[0].shape == t.chunksize


if __name__ == "__main__":
    test_chunk_iterator()
    test_dynamic_tensor_shapes()