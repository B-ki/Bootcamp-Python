import six

class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if not all(isinstance(i, float) for i in coefs):
            raise TypeError("1 coeff at least is not an int")
        if not all(isinstance(i, six.string_types) for i in words):
            raise TypeError("1 word at least is not a string")
        if len(coefs) != len(words):
            raise ValueError("Not as much coefs as words")
        x = 0
        for c, w in zip(coefs, words):
            x += c * len(w)
        return x

    def enumerate_evaluate(coefs, words):
        if not all(isinstance(i, float) for i in coefs):
            raise TypeError("1 coeff at least is not an int")
        if not all(isinstance(i, six.string_types) for i in words):
            raise TypeError("1 word at least is not a string")
        if len(coefs) != len(words):
            raise ValueError("Not as much coefs as words")
        x = 0
        for i, val in enumerate(words):
            x += len(val) * coefs[i]
        return x


words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]

print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))
