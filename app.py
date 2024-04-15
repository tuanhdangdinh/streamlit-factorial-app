import streamlit as st

from factorial import fact

def main():
    st.title('Factorial Calculator')
    n = st.number_input('Enter a number:', min_value=0, max_value=100, value=0)
    
    if st.button('Calculate'):
        result = fact(n)
        st.write(f'The factorial of {n} is {result}')

if __name__ == '__main__':
    main()