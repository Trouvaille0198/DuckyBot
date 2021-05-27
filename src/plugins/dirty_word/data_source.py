from src.utils.markov import Markov

dirty_marcov = Markov(5, r'src/data/dirty_sentences', text_type='Chinese')
dirty_marcov.save_segmentation()


def get_dirty_words():
    global dirty_marcov
    return dirty_marcov.generate_one_sentence()
