import { TestBed } from '@angular/core/testing';

import { HttpErrorInterceptor } from './http-error.interceptor';
import {MatDialog, MatDialogModule} from '@angular/material/dialog';

describe('HttpErrorInterceptor', () => {
  beforeEach(() => TestBed.configureTestingModule({
    providers: [HttpErrorInterceptor, MatDialog],
    imports: [MatDialogModule]
  }));

  it('should be created', () => {
    const interceptor: HttpErrorInterceptor = TestBed.inject(HttpErrorInterceptor);
    expect(interceptor).toBeTruthy();
  });
});
