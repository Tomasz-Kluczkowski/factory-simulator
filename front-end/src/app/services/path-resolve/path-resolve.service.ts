import {Injectable} from '@angular/core';
import {ActivatedRouteSnapshot, Resolve, RouterStateSnapshot} from '@angular/router';
import {Observable} from 'rxjs';
import {paths} from '../../configuration/app-paths';

// Credit to Vitalii Bobrov: https://medium.com/angular-in-depth/angular-smart-404-page-85a45b109fd8

@Injectable({
  providedIn: 'root'
})
export class PathResolveService implements Resolve<string | null> {

  constructor() {
  }

  resolve(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): Observable<string | null> | Promise<string | null> | string | null {
    const typoPath: string = state.url.replace('/', '');
    const threshold: number = this.getThreshold(typoPath);
    const pathsToCompare: string[] = this.getPathsToCompare(typoPath, threshold);

    if (!pathsToCompare.length) {
      return null;
    }

    this.sortByLevenshteinDistances(typoPath, pathsToCompare);
    return `/${pathsToCompare[0]}`;
  }

  getPathsToCompare(typoPath: string, threshold: number) {
    return Object.values(paths).filter(path => Math.abs(path.length - typoPath.length) < threshold);
  }

  getThreshold(path: string): number {
    if (path.length < 5) {
      return 3;
    }

    return 5;
  }

  sortByLevenshteinDistances(typoPath: string, pathsToCompare: string[]) {
    const pathsDistance = {} as { [name: string]: number };

    pathsToCompare.sort((a, b) => {
      if (!(a in pathsDistance)) {
        pathsDistance[a] = this.calculateLevenshteinDistance(a, typoPath);
      }
      if (!(b in pathsDistance)) {
        pathsDistance[b] = this.calculateLevenshteinDistance(b, typoPath);
      }

      return pathsDistance[a] - pathsDistance[b];
    });
  }

  calculateLevenshteinDistance(a: string, b: string): number {
    if (a.length === 0) {
      return b.length;
    }
    if (b.length === 0) {
      return a.length;
    }

    const matrix = [];

    // increment along the first column of each row
    for (let i = 0; i <= b.length; i++) {
      matrix[i] = [i];
    }

    // increment each column in the first row
    for (let j = 0; j <= a.length; j++) {
      matrix[0][j] = j;
    }

    // Fill in the rest of the matrix
    for (let i = 1; i <= b.length; i++) {
      for (let j = 1; j <= a.length; j++) {
        if (b.charAt(i - 1) === a.charAt(j - 1)) {
          matrix[i][j] = matrix[i - 1][j - 1];
        } else {
          matrix[i][j] = Math.min(
            matrix[i - 1][j - 1] + 1, // substitution
            matrix[i][j - 1] + 1, // insertion
            matrix[i - 1][j] + 1, // deletion
          );
        }
      }
    }

    return matrix[b.length][a.length];
  }
}
