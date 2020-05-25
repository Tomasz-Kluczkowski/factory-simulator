import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PageNotFoundComponent } from './page-not-found.component';
import {ActivatedRoute} from '@angular/router';
import {RouterTestingModule} from '@angular/router/testing';
import {of} from 'rxjs';

describe('PageNotFoundComponent', () => {
  let component: PageNotFoundComponent;
  let fixture: ComponentFixture<PageNotFoundComponent>;
  const path = '/about';

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [RouterTestingModule],
      providers: [
        {
          provide: ActivatedRoute,
          useValue: {
            data: of({path})
          }
        }
      ],
      declarations: [ PageNotFoundComponent ]
    });
  }));

  it('should create', () => {
    TestBed.compileComponents();
    fixture = TestBed.createComponent(PageNotFoundComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
    expect(component).toBeTruthy();
  });

  it('should show proposed navigation link to the user', () => {
    TestBed.compileComponents();
    fixture = TestBed.createComponent(PageNotFoundComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
    const nativeElement = fixture.debugElement.nativeElement;
    expect(nativeElement.querySelector('.page-not-found__proposed-link').textContent).toContain(
      `Did you want to navigate to: ${path} ?`
    );
  });

  it('should not show proposed navigation link to the user if path not provided', () => {
    TestBed.overrideProvider(ActivatedRoute, {
      useValue: {
        data: of({path: null})
      }
    });
    TestBed.compileComponents();
    fixture = TestBed.createComponent(PageNotFoundComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
    const nativeElement = fixture.debugElement.nativeElement;
    expect(nativeElement.querySelector('.page-not-found__proposed-link')).toBeFalsy();
  });
});
