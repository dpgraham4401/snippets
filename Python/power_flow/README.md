# Interview prep

Came up with this problem as a best-guess for the kind of work
I'll need to do for an upcoming interview.

# Problem statement

1. Load the data from a CSV file
2. Parse the data
    - Be comfortable using pandas or just going straight with the standard library
3. Clean the data
    - Find all buses with missing or invalid voltage_pu values. Drop these buses from the DataFrame.
    - Find all buses where voltage_pu is below 0.95 or above 1.05. Print their bus_id and voltage_pu.
4. Calculate new data
    - For each valid bus, calculate the net real power injection 𝑃 = gen_p − load_p. Add a new column net_p_mw to the
      buses DataFrame.
5. Be able to use group by.
    - For each from_bus, calculate the average resistance_pu of the outgoing lines.
6. Use matrices for deeper analysis
    - Create a matrix showing which buses are connected.
      Rows = from_bus, Columns = to_bus, value = 1 if connected, else 0.
7. Use numpy for matrix operations and numpy
    - For each line, calculate the impedance magnitude: |Z| = sqrt(resistance_pu^2 + reactance_pu^2).

## Data

Sample created dataset is in the data directory. The data is in csv format.