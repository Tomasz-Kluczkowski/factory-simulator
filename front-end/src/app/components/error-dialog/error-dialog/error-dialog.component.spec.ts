import {async, ComponentFixture, TestBed} from '@angular/core/testing';

import {ErrorDialogComponent} from './error-dialog.component';
import {MatIconModule} from '@angular/material/icon';
import {MatCardModule} from '@angular/material/card';
import {MatDividerModule} from '@angular/material/divider';
import {MatInputModule} from '@angular/material/input';
import {MAT_DIALOG_DATA} from '@angular/material/dialog';

describe('ErrorDialogComponent', () => {
  let component: ErrorDialogComponent;
  let fixture: ComponentFixture<ErrorDialogComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [MatIconModule, MatCardModule, MatDividerModule, MatInputModule],
      declarations: [ErrorDialogComponent],
      providers: [
        {
          provide: MAT_DIALOG_DATA,
          useValue: {
            data: {
              name: 'some error',
              url: 'http://test.api',
              message: 'error message',
              status: 404,
              statusText: 'bad thing happened',
              reason: 'for no reason really',
            }
          }
        }
      ]
    })
      .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ErrorDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
