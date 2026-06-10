// App.js
import React, { useState } from 'react';
import {
  View,
  Text,
  TouchableOpacity,
  StyleSheet,
  SafeAreaView,
  StatusBar,
} from 'react-native';

export default function App() {
  // Counter State
  const [count, setCount] = useState(0);

  // Theme State
  const [isDarkMode, setIsDarkMode] = useState(false);

  // Increment Counter
  const handleIncrement = () => {
    setCount(count + 1);
  };

  // Decrement Counter (Never Below 0)
  const handleDecrement = () => {
    if (count > 0) {
      setCount(count - 1);
    }
  };

  // Reset Counter
  const handleReset = () => {
    setCount(0);
  };

  // Toggle Theme
  const toggleTheme = () => {
    setIsDarkMode(!isDarkMode);
  };

  // Dynamic Theme Selection
  const theme = isDarkMode ? darkTheme : lightTheme;

  return (
    <SafeAreaView style={[styles.container, theme.background]}>
      <StatusBar
        barStyle={isDarkMode ? 'light-content' : 'dark-content'}
        backgroundColor={isDarkMode ? '#1f2937' : '#ffffff'}
      />

      {/* Title */}
      <Text style={[styles.title, theme.text]}>
        Digital Counter
      </Text>

      {/* Counter Display */}
      <Text style={[styles.counterText, theme.text]}>
        {count}
      </Text>

      {/* Increment & Decrement Buttons */}
      <View style={styles.buttonRow}>
        <TouchableOpacity
          style={[styles.button, styles.decrementButton]}
          onPress={handleDecrement}
        >
          <Text style={styles.buttonText}>Decrement</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={[styles.button, styles.incrementButton]}
          onPress={handleIncrement}
        >
          <Text style={styles.buttonText}>Increment</Text>
        </TouchableOpacity>
      </View>

      {/* Reset Button */}
      <TouchableOpacity
        style={[styles.button, styles.resetButton]}
        onPress={handleReset}
      >
        <Text style={styles.buttonText}>Reset</Text>
      </TouchableOpacity>

      {/* Theme Toggle Button */}
      <TouchableOpacity
        style={[styles.button, styles.themeButton]}
        onPress={toggleTheme}
      >
        <Text style={styles.buttonText}>
          {isDarkMode ? 'Switch to Light Mode' : 'Switch to Dark Mode'}
        </Text>
      </TouchableOpacity>

      {/* Current Theme */}
      <Text style={[styles.themeLabel, theme.text]}>
        Current Theme: {isDarkMode ? 'Dark Mode' : 'Light Mode'}
      </Text>
    </SafeAreaView>
  );
}

// Main Styles
const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },

  title: {
    fontSize: 30,
    fontWeight: 'bold',
    marginBottom: 20,
  },

  counterText: {
    fontSize: 70,
    fontWeight: 'bold',
    marginBottom: 30,
  },

  buttonRow: {
    flexDirection: 'row',
    marginBottom: 15,
  },

  button: {
    paddingVertical: 12,
    paddingHorizontal: 20,
    borderRadius: 10,
    marginHorizontal: 5,
    alignItems: 'center',
    justifyContent: 'center',
  },

  incrementButton: {
    backgroundColor: '#22c55e',
  },

  decrementButton: {
    backgroundColor: '#ef4444',
  },

  resetButton: {
    backgroundColor: '#6b7280',
    width: 220,
    marginBottom: 15,
  },

  themeButton: {
    backgroundColor: '#8b5cf6',
    width: 220,
    marginBottom: 15,
  },

  buttonText: {
    color: '#ffffff',
    fontSize: 16,
    fontWeight: 'bold',
  },

  themeLabel: {
    fontSize: 16,
    marginTop: 10,
  },
});

// Light Theme
const lightTheme = StyleSheet.create({
  background: {
    backgroundColor: '#ffffff',
  },
  text: {
    color: '#000000',
  },
});

// Dark Theme
const darkTheme = StyleSheet.create({
  background: {
    backgroundColor: '#1f2937',
  },
  text: {
    color: '#ffffff',
  },
});