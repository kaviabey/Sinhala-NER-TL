import pandas as pd
from sinling import SinhalaTokenizer

class SentenceSplitter:
  
    def __init__(self, df: pd.DataFrame):
     
        self.df = df
        self.tokenizer = SinhalaTokenizer()  # Initialize the Sinhala Tokenizer
    
    def split_sentences(self) -> pd.DataFrame:
     
        # Join the tokens into a single string
        text = " ".join(self.df['Token'])
        
        # Use the Sinling tokenizer to split the text into sentences
        sentences = self.tokenizer.split_sentences(text)  # This returns a list of sentences
        
        sentence_id = 1
        sentence_tokens = []
        
        # Iterate over the sentences and create sentence-wise token lists
        for sentence in sentences:
            # Split the sentence into tokens (words)
            tokens_in_sentence = sentence.split()  # Tokenize by whitespace
            
            for token in tokens_in_sentence:
                # For each token in the sentence, append it to the list with the corresponding SentenceID
                sentence_tokens.append((sentence_id, token))
            
            # Increment the sentence ID after processing each sentence
            sentence_id += 1
        
        # Create a DataFrame with SentenceID and Tokens
        sentence_df = pd.DataFrame(sentence_tokens, columns=['SentenceID','Token'])
      
        # Merge with the original DataFrame based on tokens
        merged_df = pd.concat([self.df, sentence_df['SentenceID']], axis=1)
        
        return merged_df



class Preprocessing:
    """Preprocessing class."""
    def __init__(self, df):
        self.df = df

    def remove_unknown_pos_tags(self):
        # Filter out rows where POS tag is "UNKNOWN" or "??"
        filtered_df = self.df[~self.df['Postag'].isin(['UNKNOWN', '??'])]
        return filtered_df
    
    def remove_empty_rows(self):
        """Remove rows with any empty values."""
        self.df = self.df.dropna()
        
         
    def apply_preprocessing(self):
        self.remove_unknown_pos_tags()
        self.remove_empty_rows()
        return self.df
    
