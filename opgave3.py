import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv(r"C:\Users\Victor Steinrud\Downloads\recipeData.csv", encoding='ISO-8859-1')


# Select only the numerical columns from the DataFrame
numerical_columns = df.select_dtypes(include=['number']).columns

# Specify the directory to save the plots
save_dir = r"C:\Users\Victor Steinrud\Documents\DAKI\2. semester\AI_og_DATA\plots opgave3"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)  # Create the directory if it does not exist

# Create and save a histogram for each numerical feature
for column in numerical_columns:
    plt.figure(figsize=(10, 4))  # Set the figure size for better readability
    df[column].hist(bins=30)  # You can adjust the number of bins
    plt.title(f'Histogram of {column}')  # Set the title to the name of the column
    plt.xlabel(column)  # Set the x-axis label to the name of the column
    plt.ylabel('Frequency')  # Set the y-axis label to 'Frequency'
    plt.grid(False)  # Turn off the grid to reduce visual clutter
    # Save the plot as a PNG file
    filepath = os.path.join(save_dir, f'{column}_histogram.png')
    plt.savefig(filepath)
    plt.close()  # Close the figure to free memory