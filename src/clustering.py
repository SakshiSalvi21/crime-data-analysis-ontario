"""
Clustering Module

This module contains functions for performing K-means clustering
on city crime profiles.
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


def prepare_clustering_data(df):
    """
    Prepare data for clustering analysis.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Cleaned dataframe
        
    Returns:
    --------
    pd.DataFrame
        Aggregated data ready for clustering
    """
    # Aggregate by city and violation type
    city_violations = df.groupby(['City', 'Violations'])['Value'].sum().unstack(fill_value=0)
    return city_violations


def find_optimal_clusters(X, max_clusters=6):
    """
    Find optimal number of clusters using elbow method.
    
    Parameters:
    -----------
    X : array-like
        Feature matrix
    max_clusters : int
        Maximum number of clusters to test
        
    Returns:
    --------
    list
        Inertia values for each k
    """
    inertias = []
    K_range = range(1, max_clusters + 1)
    
    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X)
        inertias.append(kmeans.inertia_)
    
    return inertias


def perform_clustering(df, n_clusters=3):
    """
    Perform K-means clustering on city data.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Cleaned dataframe
    n_clusters : int
        Number of clusters
        
    Returns:
    --------
    tuple
        (cluster_labels, pca_result, kmeans_model, scaler)
    """
    # Prepare data
    X = prepare_clustering_data(df)
    
    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Apply K-Means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(X_scaled)
    
    # Apply PCA for visualization
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    
    return cluster_labels, X_pca, kmeans, scaler


def plot_clusters(X_pca, cluster_labels, city_names, save_path=None):
    """
    Visualize clusters using PCA-reduced data.
    
    Parameters:
    -----------
    X_pca : array-like
        PCA-transformed data
    cluster_labels : array-like
        Cluster assignments
    city_names : list
        List of city names
    save_path : str, optional
        Path to save the figure
    """
    plt.figure(figsize=(10, 8))
    
    colors = ['blue', 'red', 'green', 'orange', 'purple']
    
    for i in range(len(np.unique(cluster_labels))):
        mask = cluster_labels == i
        plt.scatter(X_pca[mask, 0], X_pca[mask, 1], 
                   c=colors[i], label=f'Cluster {i}', s=100, alpha=0.7)
    
    # Add city labels
    for i, city in enumerate(city_names):
        plt.annotate(city, (X_pca[i, 0], X_pca[i, 1]), 
                    xytext=(5, 5), textcoords='offset points', fontsize=9)
    
    plt.xlabel('First Principal Component', fontsize=12)
    plt.ylabel('Second Principal Component', fontsize=12)
    plt.title('K-Means Clustering of Ontario Cities by Crime Profile', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()


def get_cluster_profiles(df, cluster_labels):
    """
    Get detailed profiles for each cluster.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Cleaned dataframe
    cluster_labels : array-like
        Cluster assignments
        
    Returns:
    --------
    dict
        Dictionary with cluster profiles
    """
    X = prepare_clustering_data(df)
    X['Cluster'] = cluster_labels
    
    profiles = {}
    for cluster in np.unique(cluster_labels):
        cluster_data = X[X['Cluster'] == cluster]
        cities = cluster_data.index.tolist()
        avg_crime = cluster_data.drop('Cluster', axis=1).sum(axis=1).mean()
        
        profiles[f'Cluster_{cluster}'] = {
            'cities': cities,
            'avg_total_crime': avg_crime,
            'risk_level': ['Low', 'Moderate', 'High'][cluster] if cluster < 3 else 'Unknown'
        }
    
    return profiles


if __name__ == '__main__':
    # Example usage
    import data_cleaning as dc
    
    df = dc.clean_data('../Crime Dataset for Data Acquisition.csv')
    
    # Perform clustering
    labels, X_pca, kmeans, scaler = perform_clustering(df, n_clusters=3)
    
    # Get city names
    X = prepare_clustering_data(df)
    city_names = X.index.tolist()
    
    # Plot clusters
    plot_clusters(X_pca, labels, city_names)
    
    # Get profiles
    profiles = get_cluster_profiles(df, labels)
    for cluster, profile in profiles.items():
        print(f"\n{cluster}:")
        print(f"  Cities: {', '.join(profile['cities'])}")
        print(f"  Risk Level: {profile['risk_level']}")
        print(f"  Avg Total Crime: {profile['avg_total_crime']:,.0f}")
